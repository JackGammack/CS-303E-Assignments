#  File: DNA.py

#  Description: Prints the longest common sequences between two DNA strands.

#  Student Name: Jack Gammack

#  Student UT EID: jg64475

#  Course Name: CS 303E

#  Unique Number: 51345

#  Date Created: 10/26/2017

#  Date Last Modified: 10/26/2017

def main ():

  print('Longest Common Sequences')
  # open file for reading
  in_file = open ("./dna.txt", "r")

  # read the number of pairs
  num_pairs = in_file.readline ()
  num_pairs = num_pairs.strip()
  num_pairs = int (num_pairs)

  # read each pair of dna strands
  for i in range (num_pairs):
      
    d1=[]
    d2=[]
    
    st1 = in_file.readline()
    st2 = in_file.readline()

    st1 = st1.strip()
    st2 = st2.strip()

    st1 = st1.upper ()
    st2 = st2.upper ()

    # order the strands by size
    if (len(st1) > len (st2)):
      dna1 = st1
      dna2 = st2
    else:
      dna1 = st2
      dna2 = st1

    # get all substrands of dna2
    # put all possible substrands of dna2 in d2[], longest substrand first
    wnd = len (dna2)
    while (wnd > 1):
      start_idx = 0
      while ((start_idx + wnd) <= len(dna2)):
        sub_strand = dna2[start_idx: start_idx + wnd]
        d2.append(sub_strand)
        # move the window by one
        start_idx += 1
      # decrease the window size
      wnd = wnd - 1

    # get all substrands of dna1
    # put all possible substrands of dna1 in d1[], longest substrand first
    wnd = len (dna1)
    while (wnd > 1):
      start_idx = 0
      while ((start_idx + wnd) <= len(dna1)):
        sub_strand = dna1[start_idx: start_idx + wnd]
        d1.append(sub_strand)
        # move the window by one
        start_idx += 1
      # decrease the window size
      wnd = wnd - 1

    #compare the two lists of substrands
    #prints only the first substrand of d2 that matches d1, because the
      #substrand lengths are in descending order, so this will be the longest.
      #Only prints the first one and breaks afterwards according to the extra credit
    maxlength=0
    printed = False
    for strands2 in d2:
        for strands1 in d1:
            if( strands2 == strands1 ):
                print()
                print('Pair ' +str(i+1) + ': ' + strands1)
                printed = True
                break #extra credit
        if (printed):
            break #extra credit
    if ( not printed ):
        print()
        print( 'Pair ' +str(i+1) + ': ' +'No Common Sequence Found' )
        

  # close the file
  in_file.close()

main()
