from heuristic.classes import Problem
from heuristic.constants import MAX_STACK_INDEX


def demand_total(problem: Problem, solver):
    """
    Ensures total demands 1 on truck 1 less after customer.
    """
    for customer_1 in range(1, problem.num_customers + 1):
        demand_to_customer = solver.sum(
            solver.demand_binary[
                customer_2, customer_1, stack, index, destination, 0] -
            solver.demand_binary[
                customer_1, customer_2, stack, index, destination, 0]
            for customer_2 in range(problem.num_customers + 1)
            for stack in range(problem.num_stacks)
            for index in range(MAX_STACK_INDEX)
            for destination in range(problem.num_customers + 1))
        solver.add_constraint(demand_to_customer == 1)