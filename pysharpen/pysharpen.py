import sys
from pathlib import Path
from .worker import Worker
from .methods import IHS, Brovey, GIHS

def run_cli():
    """
    CLI: python worker.py panchrom_name.tif multispectral_name.tif out_name.tif method
    method = <ihs|brovey>
    """
    if len(sys.argv) < 4:
        print ("Usage: pysharpen panchrom_name.tif multispectral_name.tif out_name.tif <ihs|brovey> [resampling=bilinear/cubic]")
        exit(0)
    pan = sys.argv[1]
    ms = sys.argv[2]
    out = sys.argv[3]
    
    if len(sys.argv) == 4:
        method = IHS
    else:
        if sys.argv[4].lower() == 'ihs':
            method = IHS
        elif sys.argv[4].lower() == 'brovey':
            method = Brovey
        elif sys.argv[4].lower() == 'gihs':
            method = GIHS
        else:
            print("Method is incorrect")
            exit(0)
            
    if len(sys.argv) == 5:
        resampling = 'bilinear'
    else:
        resampling = sys.argv[5]

    if not Path(pan).exists():
        print("Panchrom file does not exist")
        exit(0)
    if not Path(ms).exists():
        print("MS file does not exist")
        exit(0)

    #try:
    w = Worker(method=method, resampling=resampling)
    w.process_single(pan, ms, out)
    #except Exception as e:
     #   print('Error in pansharpening')
    #    print(str(e))
     #   exit(-1)

if __name__ == "__main__":
    run_cli(sys.argv)