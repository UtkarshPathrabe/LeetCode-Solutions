class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        # 4, 1 => log(4)
        # 4, 2 => log(4/2)

        # When there is only 1 chance to test, we need at least log_2(buckets) pigs to test
        # When there is n chance to test, the optimum strategy requires finding the pig at 
        # the last test. For example, buckets = 5, n_tests = 2, if we have two pigs, we can
        # do 1,2 for pig 1, 3,4 for pig 2. If both die, it's 5, if one of them die, we can
        # use the other pig to test. If Buckets = 6, naively, we can do 1,2,3 for pig 1, and 
        # 3,4,5 for # pig 2. If one dies, we still have 3 to choose which requires another pig,
        # increasing the pigs needed to 3. If we do 1,2,3 for pig 1 and 3,4,5 for pig 2, if
        # neither die, it's 6; if both die, it's 3; if one die, we can test with the other one.
        # this means that pigs required is still 2. For buckets = 7, we can do 1,2,3,4 for 
        # pig 1, 4,5,6 for pig 2.
        #
        # At each test, we can choose how many buckets to elmintate and how many pigs alive
        # for the next test. We can do dfs to find the methods to use the least pig. If we
        # have n buckets, we know that the upper bound is log2(n). We know that the lower
        # bound is 1. We can try all numbers of pigs and find the pigs alive after 1 round.
        # The minimum number of pigs surviving is the overlap of the buckets for each pig.
        # Each time we want to mix buckets so that each combination of the liveness of the pigs
        # corresponds to 1 section of buckets containing posion. If all buckets goes out
        # 1*6 => 1,2,3 | 2,3,4 | 3,4,5
        # 
        # buckets = 4, test = 2: ln_2(buckets / 2)
        # buckets = 5, test = 2

        # Instead of counting how many pigs are alive for each test case and figuring out if the
        # pigs are enough, we can try to figure out how many combinations of states does the sum
        # of i = 1, 2.., n pigs could represent.
        # 

        # if buckets <= 2:
        #     return 1

        n_tests = minutesToTest // minutesToDie
        print(math.log(buckets) / math.log(n_tests + 1))
        return math.ceil(round(math.log(buckets) / math.log(n_tests + 1), 10))