import upf
from upf.shortcuts import *

from ptc.problem import TestCaseProblem

class Basic1(TestCaseProblem):

    def __init__(self, expected_version):
        TestCaseProblem.__init__(self, expected_version)

    def get_problem(self):
        x = Fluent('x')
        y = Fluent('y')
        a = InstantaneousAction('a')
        a.add_precondition(y)
        a.add_effect(x, True)
        a.add_effect(y, False)
        problem = Problem('basic')
        problem.add_fluent(x)
        problem.add_action(a)
        problem.set_initial_value(x, False)
        problem.set_initial_value(y, True)
        problem.add_goal(x)
        return problem

    def get_description(self):
        return 'Just a basic test'

    def version(self):
        return 1