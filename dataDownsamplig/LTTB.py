'''
Created on 08.09.2017

@author: p.cretu
'''
import numpy

class LTTB(object):
    '''
    '''
    def __init__(self):
        '''
        '''
        pass
        
    def _areas_of_triangles(self, a, bs, c):
        '''
        
        Calculate areas of triangles from duples of vertex coordinates.
        Uses implicit numpy broadcasting along first axis of ``bs``.
        
        **input**: a: value
                   bs: array
                   c: value
                   
        **return**: numpy array
                    Array of areas of shape (len(bs),)
            
        '''
        
        bs_minus_a = bs - a
        a_minus_bs = a - bs
        return 0.5 * abs((a[0] - c[0]) * (bs_minus_a[:, 1])
                         - (a_minus_bs[:, 0]) * (c[1] - a[1]))
        
        
        
    def downsample(self, data, n_out):
        '''
        
        Downsample data to n_out points using the LTTB algorithm.
        
        **input**: data: array of size 2 x n; first array has to be
                         sorted, should be time or increasing 
                         numbering
                   n_out: resolution - the new length of the data,
                          the downsammple result length
                          3 <= n_out <= length data
              
        **return**: array of shape 2 x n_out; type: numpy array 
        
        Reference
        ---------
        Sveinn Steinarsson. 2013. Downsampling Time Series for Visual
        Representation. MSc thesis. University of Iceland.
        
        '''
        
        # if the input data length is greater than the desired resolution
        # return the data itself
        if n_out >= data.shape[0]:
            return data
        
        # Validate input
        if len(data.shape) == 1:
            indexes = numpy.arange(data.shape[0])
            data = numpy.asarray([indexes, data])
        if len(data.shape) == 2 and data.shape[0]>2:
            raise ValueError('data should have 2 columns')
        
        data = data.T
        if any(data[:, 0] != numpy.sort(data[:, 0])):
            raise ValueError('data should be sorted on first column')

        if n_out < 3:
            raise ValueError('Can only downsample to a minimum of 3 points')
        
        # Split data into bins
        n_bins = n_out - 2
        data_bins = numpy.array_split(data[1: len(data) - 1], n_bins)
    
        # Prepare output array
        # First and last points are the same as in the input.
        out = numpy.zeros((n_out, 2))
        out[0] = data[0]
        out[len(out) - 1] = data[len(data) - 1]
    
        # Largest Triangle Three Buckets (LTTB):
        # In each bin, find the point that makes the largest triangle
        # with the point saved in the previous bin
        # and the centroid of the points in the next bin.
        for i in range(len(data_bins)):
            this_bin = data_bins[i]
    
            if i < n_bins - 1:
                next_bin = data_bins[i + 1]
            else:
                next_bin = data[len(data) - 1:]
    
            a = out[i]
            bs = this_bin
            c = next_bin.mean(axis=0)
    
            areas = self._areas_of_triangles(a, bs, c)
    
            out[i + 1] = bs[numpy.argmax(areas)]
            
            
    
        return out.T