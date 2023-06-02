class Calculator:
    def multiplication(self, *args):
        res = 1
        for i in args:
            res *= i

        return res