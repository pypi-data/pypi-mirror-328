from __future__ import annotations
from typing import Any, List
import textwrap
from .. import dsl, std
from ..std import rel
from ..metamodel import Builtins

rel_sv = rel._tagged(Builtins.SingleValued)

# --------------------------------------------------
# SolverModel object.
# --------------------------------------------------

class SolverModel:
    def __init__(self, graph:dsl.Graph):
        self.graph = graph
        self.id = dsl.next_id()
        self.scope = f"solvermodel{self.id}_"
        scope = self.scope
        self.Variable = dsl.Type(graph, "variables", scope=scope)
        self.MinObjective = dsl.Type(graph, "min_objectives", scope=scope)
        self.MaxObjective = dsl.Type(graph, "max_objectives", scope=scope)
        self.Constraint = dsl.Type(graph, "constraints", scope=scope)
        self.components = [
            (self.MinObjective, "minimization objectives"),
            (self.MaxObjective, "maximization objectives"),
            (self.Constraint, "constraints"),
        ]
        self.solve_output = dsl.RelationNS([], f"{scope}solve_output")
        self.is_solved = False

        # Install model helpers.
        self.graph.install_raw(textwrap.dedent(f"""
            @inline
            def _solverlib_ho_appl(op, {{R}}, s): rel_primitive_solverlib_ho_appl(R, op, s)

            @inline
            def _solver_unwrap({{R}}, h, x...): exists((v) | R(v, x...) and pyrel_unwrap(v, h))

            declare {scope}variable_name
            declare {scope}component_name
            declare {scope}serialized

            def {scope}component_string(h, s):
                rel_primitive_solverlib_print_expr(
                    {scope}serialized[h], _solver_unwrap[{scope}variable_name], s
                )

            def {scope}specialized_components(t, h, s):
                exists((v) | {{
                    (:min_objective, {scope}min_objectives);
                    (:max_objective, {scope}max_objectives);
                    (:constraint, {scope}constraints);
                    }}(t, v) and pyrel_unwrap(v, h) and {scope}serialized(v, s)
                )

            declare {scope}solve_output
        """))
        return None

    # Add an entity to the variable set, (optionally) set a string name from the
    # arguments and add domain constraints on the variable.
    def variable(self, var, name_args:List|None=None, type:str|None=None,
        lower:int|float|None=None, upper:int|float|None=None, fixed:int|float|None=None
    ):
        if type not in {"integer", "zero_one", None}:
            raise Exception(f"Invalid domain type: {type}.")
        var.set(self.Variable)

        # Set variable name.
        if name_args:
            var.set(**{f"{self.scope}variable_name": make_string(name_args)})

        # Add domain constraints.
        cons = []
        if fixed is not None:
            cons.append(eq(var, fixed))
        if type == "zero_one":
            cons.append(zero_one(var))
        if lower is not None and upper is not None:
            if type == "integer":
                cons.append(integer_interval(var, lower, upper))
            else:
                # cons.append(interval(var, lower, upper)) TODO(coey)
                cons.append(gte(var, lower))
                cons.append(lte(var, upper))
        else:
            if type == "integer":
                cons.append(integer(var))
            if lower is not None:
                cons.append(gte(var, lower))
            if upper is not None:
                cons.append(lte(var, upper))
        if len(cons) == 1:
            self.constraint(cons[0])
        elif len(cons) > 1:
            self.constraint(and_(*cons))
        return var

    # Get variable string name.
    def variable_name(self, var):
        return std.alias(getattr(var, f"{self.scope}variable_name"), "name")

    # Add a constraint, minimization objective, or maximization objective.
    def constraint(self, expr, name_args:List|None=None):
        return self._add_component(self.Constraint, expr, name_args)

    def min_objective(self, expr, name_args:List|None=None):
        return self._add_component(self.MinObjective, expr, name_args)

    def max_objective(self, expr, name_args:List|None=None):
        return self._add_component(self.MaxObjective, expr, name_args)

    def _add_component(self, typ, expr, name_args:List|None):
        # TODO(coey) for now we create unique property names for the serialized component
        # property in order to get unique relation names in the generated Rel, otherwise
        # we have trouble tracing performance data back to the original PyRel block.
        prop = "serialized" + str(dsl.next_id())
        comp = typ.add(**{prop: _wrap_expr(expr)})
        self.graph.install_raw(f"def {self.scope}serialized {{ {self.scope}{prop} }}")
        # comp = typ.add(serialized=_wrap_expr(expr)) # TODO(coey) the simpler way.
        if name_args:
            comp.set(component_name=make_string(name_args))
        return comp

    # Get component string name.
    def component_name(self, comp):
        return std.alias(comp.component_name, "name")

    # Get serialized component string in human-readable format.
    def component_string(self, comp):
        return std.alias(comp.component_string, "string")

    # Summarize the model by printing the number of variables and components.
    # Use outside a rule/query.
    def summarize(self):
        with self.graph.query() as select:
            vars = select(std.aggregates.count(self.Variable()))
        s = f"Model has: {vars.results.iat[0, 0]} variables"
        for (c_type, c_name) in self.components:
            with self.graph.query() as select:
                exprs = select(std.aggregates.count(c_type()))
            if not exprs.results.empty:
                s += f", {exprs.results.iat[0, 0]} {c_name}"
        print(s)
        return None

    # Print the model in human-readable format. Use outside a rule/query.
    def print(self):
        with self.graph.query() as select:
            vars = select(rel.last(getattr(rel, f"{self.scope}variable_name")))
        print("variables:")
        print(vars.results.to_string(index=False, header=False))
        for (c_type, c_name) in self.components:
            with self.graph.query() as select:
                exprs = select(self.component_string(c_type()))
            if not exprs.results.empty:
                print(c_name + ":")
                print(exprs.results.to_string(index=False, header=False))
        return None

    # Solve the model given a solver and solver options. Use outside a rule/query.
    def solve(self, solver:str, **kwargs):
        self.is_solved = False
        options = kwargs
        options["version"] = 1
        options["solver"] = solver.lower()

        config = self.graph._config.props
        if "azure-latest" not in config["host"]:
            raise Exception("Solvers are only supported on Azure `latest`.")

        # Make options string.
        for k, v in options.items():
            if not isinstance(k, str):
                raise Exception(f"Invalid parameter key. Expected string, got {type(k)} for {k}.")
            if not isinstance(v, (int, float, str, bool)):
                raise Exception(
                    f"Invalid parameter value. Expected string, integer, float, or boolean, got {type(v)} for {k}."
                )
        def escape(v):
            return ("true" if v else "false") if isinstance(v, bool) else v
        options_string = "&".join([f"{key}={escape(value)}" for key, value in options.items()])

        # Run the solve query and insert the solve_output result.
        scope = self.scope
        variable_name_string = f"{scope}variable_name" if "print_format" in options else "{}"
        component_name_string = f"{scope}component_name" if "print_format" in options else "{}"

        # TODO(coey) Currently we must run a dummy query to install the pyrel rules in a separate txn
        # to the solve_output updates. Ideally pyrel would offer an option to flush the rules separately.
        self.graph.exec_raw("")
        self.graph.exec_raw(textwrap.dedent(f"""
            def delete[:{scope}solve_output]: {scope}solve_output

            @no_diagnostics(:EXPERIMENTAL)
            def insert[:{scope}solve_output]:
                rel_primitive_solverlib_extract[rel_primitive_solverlib_solve[{{
                    (:model, rel_primitive_solverlib_model_string[{{
                        (:variable, _solver_unwrap[{scope}variables]);
                        (:variable_name, _solver_unwrap[{variable_name_string}]);
                        (:expression_name, _solver_unwrap[{component_name_string}]);
                        {scope}specialized_components;
                    }}]);
                    (:options, "{options_string}");
                }}]]
        """), readonly=False)

        self.is_solved = True
        return None

    # Get scalar result information after solving.
    def __getattr__(self, name:str):
        if not self.is_solved:
            raise Exception("Model has not been solved yet.")
        if name in {"error", "termination_status", "solve_time_sec", "objective_value", "solver_version", "printed_model"}:
            val = dsl.create_var()
            getattr(self.solve_output, name)(val)
            std.alias(val, name)
            return val
        else:
            return None

    # Get variable point values after solving. If `index` is specified, get the value
    # of the variable in the return the `index`-th solution.
    def value(self, var, index:int|None=None):
        if not self.is_solved:
            raise Exception("Model has not been solved yet.")
        val = dsl.create_var()
        unwrap_var = rel_sv.pyrel_unwrap(var)
        if index:
            self.solve_output.points(unwrap_var, index, val)
        else:
            self.solve_output.point(unwrap_var, val)
        std.alias(val, "value")
        return val

# --------------------------------------------------
# Operator definitions
# --------------------------------------------------

# Builtin binary operators

def plus(left, right):
    return _make_fo_expr(10, left, right)

def minus(left, right):
    return _make_fo_expr(11, left, right)

def mult(left, right):
    return _make_fo_expr(12, left, right)

def div(left, right):
    return _make_fo_expr(13, left, right)

def pow(left, right):
    return _make_fo_expr(14, left, right)

def eq(left, right):
    return _make_fo_expr(30, left, right)

def neq(left, right):
    return _make_fo_expr(31, left, right)

def lte(left, right):
    return _make_fo_expr(32, left, right)

def gte(left, right):
    return _make_fo_expr(33, left, right)

def lt(left, right):
    return _make_fo_expr(34, left, right)

def gt(left, right):
    return _make_fo_expr(35, left, right)

# First order operators

def abs(arg):
    return _make_fo_expr(20, arg)

def exp(arg):
    return _make_fo_expr(21, arg)

def log(arg):
    return _make_fo_expr(22, arg)

def integer(arg):
    return _make_fo_expr(41, arg)

def zero_one(arg):
    return _make_fo_expr(42, arg)

def interval(arg, low, high):
    # TODO(coey) add interval operator to serialization format?
    return and_(gte(arg, low), lte(arg, high))

def integer_interval(arg, low, high):
    return _make_fo_expr(50, low, high, 1, arg)

def if_then_else(cond, left, right):
    return _make_fo_expr(60, cond, left, right)

def not_(arg):
    return _make_fo_expr(61, arg)

def implies(left, right):
    return _make_fo_expr(62, left, right)

def iff(left, right):
    return _make_fo_expr(63, left, right)

def xor(left, right):
    return _make_fo_expr(64, left, right)

def and_(*args):
    return _make_fo_expr(70, *args)

def or_(*args):
    return _make_fo_expr(71, *args)

# Aggregate operators

def sum(*args, per=[]) -> Any:
    return _make_ho_expr(80, args, per)

def product(*args, per=[]) -> Any:
    return _make_ho_expr(81, args, per)

def min(*args, per=[]) -> Any:
    return _make_ho_expr(82, args, per)

def max(*args, per=[]) -> Any:
    return _make_ho_expr(83, args, per)

def count(*args, per=[]) -> Any:
    return _make_ho_expr(84, args, per)

def all_different(*args, per=[]) -> Any:
    return _make_ho_expr(90, args, per)

# --------------------------------------------------
# Symbolic expression helpers
# --------------------------------------------------

def _make_fo_expr(*args):
    expr = rel_sv.rel_primitive_solverlib_fo_appl(*args)
    expr.__class__ = SolverExpression
    return expr

# TODO(coey) test:
# dsl.tag(rel_sv.rel_primitive_solverlib_fo_appl, Builtins.Expensive)

def _make_ho_expr(op, args, per):
    return SolverExpression(dsl.get_graph(), _ho_appl_def, [args, per, [op]])

_ho_appl_def = dsl.build.aggregate_def("_solverlib_ho_appl")

class SolverExpression(dsl.Expression):
    def __init__(self, graph, op, args):
        super().__init__(graph, op, args)

def _wrap_expr(e):
    # If expression is not known to produce a serialized expression string,
    # wrap it with the identity operation just in case
    return e if isinstance(e, SolverExpression) else _make_fo_expr(0, e)

# Symbolic expression context, in which some builtin infix operators are redefined
# TODO(coey) handle comparison chains (e.g. 0 < x < y <= 1) or throw error
class Operators(dsl.Context):
    def _supports_binary_op(self, op):
        return op in _builtin_binary_map

    def _make_binary_op(self, op, left, right):
        return _make_fo_expr(_builtin_binary_map[op], left, right)

def operators():
    return Operators(dsl.get_graph())

# Maps for Builtins operator to SolverLib operator ID
_builtin_binary_map = {
    Builtins.plus: 10,
    Builtins.minus: 11,
    Builtins.mult: 12,
    Builtins.div: 13,
    Builtins.pow: 14,
    Builtins.approx_eq: 30,
    Builtins.neq: 31,
    Builtins.lte: 32,
    Builtins.gte: 33,
    Builtins.lt: 34,
    Builtins.gt: 35,
}

# Concatenate arguments into a string separated by underscores
def make_string(args:List):
    string = args[0]
    for arg in args[1:]:
        string = rel_sv.concat(rel_sv.concat(string, "_"), arg)
    return string
