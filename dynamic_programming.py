class DynamicProgrammingMatrix:
    '''
    Dynamic Programming Matrix that automatically does wrapping modulo N
    '''
    def __init__( self, N ):
        self.N = N
        self.DPmatrix = []
        for i in range( N ):
            self.DPmatrix.append( [] )
            for j in range( N ):
                self.DPmatrix[i].append( DynamicProgrammingData() )

    def __getitem__( self, idx ):
        return self.DPmatrix[ idx ]

    def __len__( self ): return len( self.DPmatrix )

class DynamicProgrammingData:
    '''
    Dynamic programming object, with derivs and contribution accumulation.
     Q   = value
     dQ  = derivative (later will generalize to gradient w.r.t. all parameters)
     contrib = contributions
    '''
    def __init__( self ):
        self.Q = 0.0
        self.dQ = 0.0
        self.contrib = []

    def __iadd__(self, other):
        self.Q += other.Q
        return self

    def __mul__(self, other):
        if type( self ) == type( other ):
            self.Q *= other.Q
        else:
            self.Q *= other
        return self

    def __truediv__( self, other ):
        self.Q /= other
        return self

    __rmul__ = __mul__
    __floordiv__ = __truediv__
    __div__ = __truediv__