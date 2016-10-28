def sed(pattern, replace, source, dest):
    """
     takes as arguments a pattern string, a replacement string, 
     and two filenames; it should read the first file and write 
     the contents into the second file (creating it if necessary)
     If the pattern string appears anywhere in the file, it 
     should be replaced with the replacement string.

     pattern: string
     replace: string 
     source: string filename
     dest: string filename
    """
    f_in = open(source, 'r')
    f_out = open(dest, 'w')

    for line in f_in:
        new_line  = line.replace(pattern, replace)
        f_out.write(new_line)
    f_in.close()
    f_out.close()
    pass
    
pattern = 'Heu Jude'
replace = 'Hey Teresa'
source = 'sed_tester.txt'
dest = 'new_' + source
sed(pattern, replace, source, dest)

