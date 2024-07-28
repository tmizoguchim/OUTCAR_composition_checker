# OUTCAR_composition_checker

This program is for checking the compositions of OUTCAR in the current folder. This program may be useful to check the compositions of materials for generation of machine learning potentical, such as MACE.

# usage
For instance, your folder have many "OUTCAR_for_mace-***" files, then this program read "POSCAR = " lines of those OUTCARs and listed their compositions and their numbers.

``` % python OUTCAR_composition_checker ```

Be care that Line-13 (below) of this program must be changed for your "OUTCAR_**" name. Now, it is "OUTCAR_for_mace".

    files = [f for f in os.listdir(folder_path) if f.startswith('OUTCAR_for_mace')]


