def data2cov(cov_flatt):
    """
    Convert flattened data (input/output of network) of dimension [9,M,N]to covariance matirx of dimension [3,3,M,N] 

    Parameters
    ----------
    cov_flatt : flattened covariance matrix to be converted
    
    Returns
    -------
    cov: covariance matrix in original shape

    """
    
    cov = np.zeros([3,3,cov_flatt.shape[1],cov_flatt.shape[2]],dtype = 'cfloat')
    cov[0,0,:,:] = cov_flatt[0,:,:] + 1j*np.zeros([cov_flatt.shape[1],cov_flatt.shape[2]])
    cov[1,1,:,:] = cov_flatt[1,:,:] + 1j*np.zeros([cov_flatt.shape[1],cov_flatt.shape[2]])
    cov[2,2,:,:] = cov_flatt[2,:,:] + 1j*np.zeros([cov_flatt.shape[1],cov_flatt.shape[2]])
    cov[0,1,:,:] = cov_flatt[3,:,:] + 1j*cov_flatt[6,:,:]
    cov[0,2,:,:] = cov_flatt[4,:,:] + 1j*cov_flatt[7,:,:]
    cov[1,2,:,:] = cov_flatt[5,:,:] + 1j*cov_flatt[8,:,:]
    cov[1,0,:,:] = np.ma.conjugate(cov[0,1,:,:])
    cov[2,0,:,:] = np.ma.conjugate(cov[0,2,:,:])
    cov[2,1,:,:] = np.ma.conjugate(cov[1,2,:,:])
                    
    return cov
    