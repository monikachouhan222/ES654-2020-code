
def entropy(Y):
    
    values,counts=np.unique(Y, return_counts=True)
    prob=counts/counts.sum()
    for i in prob
         entropy=entropy-prob*np.log(prob)
    return float(entropy)

def gini_index(Y):
    """
    Function to calculate the gini index

    Inputs:
    > Y: pd.Series of Labels
    Outpus:
    > Returns the gini index as a float
    """
    pass

def information_gain(Y, attr):
    
    
    if attr.dtype='catgory'
            values=np.unique(attr)
            for v in values
                i=0
                for index in attr
                   if atrr[index]=values
                       Yv[i]=Y[index]
                        i++ 
                totalentropy+=Len(Yv)/Len(Y)*entropy(Yv)
    gain=entropy(Y)-totalentropy
    else
         
         
    Function to calculate the information gain
    
    Inputs:
    > Y: pd.Series of Labels
    > attr: pd.Series of attribute at which the gain
    Outputs:
    > Return the information gain as a float
    """
    pass
