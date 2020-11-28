# -*- coding: utf-8 -*-

from wikideengen import WikiScrapper as ws
import sys

if __name__ == "__main__":

    cmd_str = ['--i=',
               '--o=',
               '--d=',
               '--n=',
               '--s=']

    cmds = len(sys.argv)

    if cmds <= 1:
        print("No arguments given.\nPossible arguments:")
        print('\t--i= input filename or wiki title e.g. sometext.txt or Apfel\n',
              '\t--o= outfile filename e.g. somecsv.csv\n',
              '\t--d= delimiter character e.g. ;\n',
              '\t--n= no of translations e.g. 1\n',
              '\t--s= source of de wiki or local\n',
              'cmd sample with default values: \n',
              '\t python.exe generate.py --i=Apfel --o= Apfel.csv --d=; --n=1 --s=wiki\n')
        print("Running with default values...")

    # default values
    title = "Apfel"
    filename = "Apfel.csv"
    delim = ';'
    tno = 1
    src = 'wiki'

    for cmd in sys.argv:
        print(cmd)
        if cmd_str[0] in cmd:
            title = cmd[4:]
        elif cmd_str[1] in cmd:
            filename = cmd[4:]
        elif cmd_str[2] in cmd:
            delim = cmd[4:]
        elif cmd_str[3] in cmd:
            tno = cmd[4:]
        elif cmd_str[4] in cmd:
            src = cmd[4:]

    print('title\t', title)
    print('filename\t', filename)
    print('delim\t', delim)
    print('tno\t', tno)
    print('src\t', src)

    ws.generate_csv(title=title, file_name=filename, separator=delim, translations=tno, src=src)

