import random


class ga_param():

    # class for handling conversion between decimal and binary
    # for each genetic algorithm parameter
    # michael.lensi@ruralsourcing.com

    def __init__(self, p0, pF, pD):
        self.p0 = p0
        self.pF = pF
        self.pD = pD
        print (self)

        self.num_items = (pF - p0) / pD + 1
        self.num_items = int(self.num_items)

        self.max_bits = len("{0:b}".format(self.num_items))

        self.items_list = []
        for i in range(self.num_items):
            self.items_list.append(p0 + pD*i)


    def __str__(self):
        return f"{self.p0} : {self.pD} : {self.pF}"

    
    def get_rand_item(self):
        return random.choice(self.items_list)


    def get_rand_item_binary(self):
        # ri = random.randrange(self.num_items)
        # use bit-space, not index-space
        ri = random.randrange((2**self.max_bits) - 1)
        return "{0:b}".format(ri).zfill(self.max_bits)
        

    def binary_to_item(self, b):
        di = int(b, 2)
        # now map from bit-space to index-space (next two LOC)
        di = di * self.num_items / (2**self.max_bits)
        di = round(di)
        return self.items_list[di]


    
class param_pool():

    # class for constructing a complete chromosome (solution)
    # from all GA parameters
    # michael.lensi@ruralsourcing.com

    def __init__(self):
        self.pool = [];
        

    def add_param(self, ga_param):
        self.pool.append(ga_param)


    def create_rand_solution(self):
        soln = '';
        for p in self.pool:
            soln += p.get_rand_item_binary()
        return soln

    
    def solution_to_decimal(self, soln):
        soln_dec = []
        pi0 = 0
        pif = 0
        for p in self.pool:
            pif += p.max_bits
            d = p.binary_to_item(soln[pi0:pif])
            soln_dec.append(d)
            pi0 += p.max_bits
        return soln_dec

            

def init_generation(pool, num_chrom_per_gen):
    # michael.lensi@ruralsourcing.com
    G = []
    for i in range(num_chrom_per_gen):
        soln = pool.create_rand_solution()
        G.append(soln)
    return G



def eval_fitnesses(pool, fit, G):
    # fit example:
    # fit = lambda s: 6000.0 - abs(s[0]**2 + s[1]**2)
    # michael.lensi@ruralsourcing.com
    fitnesses = []
    for soln in G:
        soln_dec = pool.solution_to_decimal(soln)
        fitnesses.append(fit(soln_dec))
    return fitnesses



def new_generation(G, fitnesses, sr=0.5, mr=0.05):

    # Create new generation newG from G using crossover and mutation.
    # sr: survival rate, default 50%
    # mr: mutation rate (per bit), default 5%
    # michael.lensi@ruralsourcing.com
    #u = len(G) * len(G[0])  # size of indep. rand var pop for mr
    #mr_birthday = 1.2 * u**(1/2) / u  # consider this for default mr
    

    # sort G by fitnesses... how will Thomas Jefferson find his next mistresses?
    G = [x for _,x in sorted(zip(fitnesses, G), reverse=True)]
         
    # newG = []
    # newG.append(G[0])  # elitism

    survG = G[:int(sr*len(G))]
    # Consider not preserving any survivors through crossover round;
    # only allow to mate.
    # Note, even so, these are fair game in mutation round (further note: elitism on).
    newG = survG[:]  # newG + survG


    print( "\nCrossover, then Mutation:" )
    # CROSSOVER
    for i in range(len(G) - len(survG)):  # - 1):
         r1 = random.randrange(len(survG))
         r2 = random.randrange(len(survG))
         if r1 == r2:
             r2+=1
             if r2 >= len(survG):
                 r2 = r1 - 1
         c = random.randrange(1, len(survG[r1]))  # crossover point
         new_soln = survG[r1][:c] + survG[r2][c:]
         newG.append(new_soln)

         # c->      || 6
         # r1: 100010000
         # r2: 100100101
         #  3: 100010101
         spc = ' ' * c
         print( "c->{0}|| {1}".format(spc, c) )
         print( "r1: {0}".format(survG[r1]) )
         print( "r2: {0}".format(survG[r2]) )
         print( " 3: {0} CHROM {1}".format(new_soln, len(survG)+i) )


    # MUTATION
    num_total_bits = len(newG) * len(newG[0])
    num_mutated_bits = int( num_total_bits * mr )
    for i in range(num_mutated_bits):
        total_bit = random.randrange(num_total_bits)
        # print(total_bit)
        chrom = int( total_bit / len(newG[0]) )
        bit = int( total_bit % len(newG) / len(newG) * len(newG[0]) )
        # elitism
        if chrom==0:
            chrom=1
        # continue
        if newG[chrom][bit] == '0':
            newG[chrom] = newG[chrom][:bit] + '1' + newG[chrom][bit+1:]
        else:
            newG[chrom] = newG[chrom][:bit] + '0' + newG[chrom][bit+1:]
        print( f"mutation: chrom {chrom}, bit {bit}" )

    print( "elitism is {0}".format(G[0] == newG[0]) )  # confirm elitism


    return newG
    

