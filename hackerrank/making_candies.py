import math


class CandyFactory:

    def __init__(self, m, w, p, n):
        self.balance = 0
        self.m = m
        self.w = w
        self.p = p
        self.n = n
        self.passes = 0
        self.last_prod = self.m * self.w
        self.curr_prod = self.m * self.w

    def make(self, passes = 1):
        self.last_prod = self.m * self.w
        self.curr_prod = self.m * self.w
        self.balance += self.curr_prod * passes
        print('making +', self.curr_prod, ' $:', self.balance, 'in passes of:', passes)

    def max_purchase_items(self, init_balanace = None):
        if not init_balanace:
            init_balanace = self.balance
        return math.floor(init_balanace / self.p)

    def buy_projection(self, init_balanace = None, limit = math.inf):
        if not init_balanace:
            init_balanace = self.balance
        new_m = 0
        new_w = 0
        mppi = min(limit, self.max_purchase_items(init_balanace))
        resources = self.m + self.w + mppi
        half_resource = math.ceil(resources / 2)
        if self.m > self.w:
            new_m = max(self.m, half_resource)
            new_w = resources - half_resource
        else:
            new_m = max(self.w, half_resource)
            new_w = resources - half_resource
        return mppi, new_m, new_w

    def buy(self):
        mppi, new_m, new_w = self.buy_projection()
        self.balance -= mppi * self.p
        print('buying m:', new_m - self.m)
        print('buying w:', new_w - self.w)
        self.m = new_m
        self.w = new_w
        self.curr_prod = self.m * self.w

    def target_reached(self):
        return (self.balance >= self.n)

    def jump(self, passes):
        print('jumping of', passes)
        print('from $', self.balance)
        self.make(passes)
        self.pass_(passes)
        print('to $', self.balance)

    def strategy(self):
        self.curr_prod = self.m * self.w
        days_to_next_buy = math.ceil(max(self.p - self.balance, 0) / self.curr_prod)

        if days_to_next_buy == 0:
            return True

        if days_to_next_buy > 1:
            self.jump(days_to_next_buy)
            return True

        new_balanace = self.balance + days_to_next_buy * self.curr_prod
        _, new_m, new_w = self.buy_projection(new_balanace)
        next_prod = new_m * new_w
        days_at_current_rate = math.ceil(self.n - self.balance / self.curr_prod)
        days_at_next_rate = math.ceil((self.n - self.balance - next_prod) / next_prod) + days_to_next_buy

        if days_at_current_rate > days_at_next_rate:
            return False
        else:
            return True

    def pass_(self, passes = 1):
        self.passes += passes

    def getPasses(self):
        return self.passes

    def __str__(self):
        return f'candies:{self.balance}, m:{self.m}, w:{self.w}, lp:{self.last_prod}, cp:{self.curr_prod}, pass:{self.passes}'


def minimumPasses(m, w, p, n):

    cf = CandyFactory(m, w, p, n)

    while not cf.target_reached():
        print(cf)
        cf.make()
        print(cf.target_reached())
        if cf.target_reached():
            cf.pass_()
            break
        if cf.strategy():
            cf.buy()
        cf.pass_()
        print(cf)
        print()

    return cf.getPasses()




    '''
    #m: number of machines
    #w: number of workers
    #p: purchase or hire cost in candy
    #n: candies to accumulate

    days = 0
    candies = 0
    answer = math.ceil(n / (m * w))
    run = math.inf

    while days < n:

        day = 0 if (m > math.inf / w) else (p - candies) / (m*w)

        if step < 0:
            mw = candy / p
            if m >= w + mw:
                w += mw
            elif w >= m + mw:
                m += mw
            else:
                total = m + w + mw
                m = total /2
                w = total -m
            candy %= p
            day = 1

        days += day

        if day * m > math.inf / w:
            candies = math.inf
        else:
            candy += step * m * w
            run = min(run, passes + math.ceil(n - candies) / (m * w))

    return min(days, run)
    '''

    '''


        # let's jump coupe of days to the point we have money to invest
        if p > candies:
            daysNeeded = math.ceil((p - candies) / (m * w))
            candies += daysNeeded * m * w
            days += daysNeeded

        # diff between no of machines and workers
        diff = abs(m - w)
        # how many we could buy
        available = candies // p
        # how many we actually buy
        purchased = min(diff, available)

        if m < w:
            # buy machines
            m += purchased
        else:
            # buy workers
            w += purchased

        # how much is left
        rest = available - purchased
        m += rest // 2
        w += rest - rest // 2
        candies -= available * p

        # generation
        candies += m * w
        days += 1

        remainingCandies = max(n - candies, 0)
        answer = min(answer, days + math.ceil(remainingCandies / (m * w)))

    return answer

    '''



#print(minimumPasses(3,1,2,12), ' expected: 3')
print(minimumPasses(1,1,6,45), ' expected: 16')
