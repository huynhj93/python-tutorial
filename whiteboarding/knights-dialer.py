graph = [
  [1,2],
  [3],
  [3],
  []
]

def yield_sequences(startPos, graph, sequence=None):
    # print(graph)
    if sequence is None:
        sequence = [startPos]
    
    if startPos == len(graph) - 1:
        yield sequence
        return

    for neighbor in graph[startPos]:
        yield from yield_sequences(
            neighbor, graph, sequence + [neighbor])


def get_sequences(graph):
    sequences = []
    # for coord in graph:
    for sequence in yield_sequences(0, graph):
        sequences.append(sequence)
    return sequences

print(get_sequences(graph))















# def count_sequences(start_position, num_hops):                
#     prior_case = [1] * 10                                     
#     current_case = [0] * 10                                   
#     current_num_hops = 1                                                            
#     while current_num_hops <= num_hops:                       
#         current_case = [0] * 10                               
#         current_num_hops += 1
#         print('============')                                 
#         print('current num hops is', current_num_hops)                                                      
#         for position in range(0, 10):
#             print('**********')
#             print('positin is', position)                         
#             for neighbor in neighbors(position):
#                 print('-----------')
#                 print('neighbor is', neighbor)              
#                 print('prior case in neighbor loop', prior_case)
#                 current_case[position] += prior_case[neighbor]
#                 print('current casd ein neightbor loop', current_case)

#         prior_case = current_case                             
#     print('done prior case', prior_case)                       
#     print('done prior case', current_case)                       
#     print('dpme prior case', current_num_hops)                                    
#     return current_case[start_position]


# count = count_sequences(4,2)
# print(count)

# def yieldSequences(startPos, numHops, seq=None):
#   print('a')
#   if seq is None:
#     print('is none')
#     print(startPos)  
#     seq = [startPos]
#     print('after')

#   if numHops == 0:
#     print('is zero')
#     yield seq
#     return
#   for neighbor in neighbors(startPos):
#     yield from yieldSequences(neighbor, numHops - 1, seq + [neighbor])
    
# def getSequences(startPos, numHops):
#   sequences = []
#   for seq in yieldSequences(startPos, numHops):
#     sequences.append(seq)
#   return sequences

# sequences = getSequences(4,2)
# print(sequences)































# def yieldSequences(startCoord, numHops, seq = NONE):
#   if seq is NONE
#     seq = [startCoord]
#   if numHops == 0
#     yield seq
#     return
#   for neighbor in neighbors(startCoord)
#     seq = 

# def countSequences(coord, numHops):
#   numSeq = 0
#   for sequence in yieldSequences(coord, numHops):
#     numSeq += 1
#   return numSeq


# def permute(inputData, outputSoFar=[], stack = 1, iteration = 1):
#     print('=======', inputData, outputSoFar, '======', 'stack begin', stack)
#     outputSizeToReach = len(inputData)
#     for elem in inputData:
#         # print('- iteration begin', iteration, '-', elem)
#         print('- iteration begin', iteration, '-', elem, outputSoFar)
#         iteration += 1
#         if elem not in outputSoFar:
#             outputSoFar.append(elem)
#             # print('output', outputSoFar)
#             if len(outputSoFar) == outputSizeToReach:
#                 print('end', outputSoFar)
#             else:
#                 permute(inputData, outputSoFar, stack + 1)  # --- Recursion
#             outputSoFar.pop()
#         # iteration -=1
#         print("- iteration end", iteration - 1, '-', inputData, outputSoFar)
#     # print('-- end loop --')
#     print('== returnining to stack', stack - 1, '==')

# permute([1, 2, 3])


# def permute(inputData, outputSoFar=[]):
#     outputSizeToReach = len(inputData)
#     for elem in inputData:
#         if elem not in outputSoFar:
#             outputSoFar.append(elem)
#             if len(outputSoFar) == outputSizeToReach:
#                 yield outputSoFar
#             else:
#                 for v in permute(inputData, outputSoFar):
#                     yield v
#             outputSoFar.pop()

# for i in permute([1,2,3]):
#   print(i)  # or whatever else you want to do with it



# def permute(inputData, outputSoFar = []):
#   outputSizeToReach = len(inputData)
#   if len(outputSoFar) == outputSizeToReach:
#     print(outputSizeToReach)
#     return
#   else:
#     for num in inputData:
#       if num not in outputSoFar:
#         outputSizeToReach.append(num)
#         permute( )
# permute([1,2,3])


# function permute(inputData, outputSoFar=[], stack = 1, iteration = 1) {
#     console.log('=======', inputData, outputSoFar, '======', 'stack begin', stack)
#     debugger
#     outputSizeToReach = inputData.length
#     for (var elem of inputData) {
#         // print('- iteration begin', iteration, '-', elem)
#         console.log('- iteration begin', iteration, '-', elem, outputSoFar)
#         iteration += 1
#         if(!outputSoFar.includes(elem)) {
#             outputSoFar.push(elem)
#             // # print('output', outputSoFar)
#             if(outputSoFar.length == outputSizeToReach) {
#               console.log('end', outputSoFar)
#             } else {
#                 console.log("- iteration end", '-', inputData, outputSoFar)
#                 permute(inputData, outputSoFar, stack + 1)
#             }
#         }
#     }
#     // print('-- end loop --')
#     console.log('== returnining to stack', stack - 1, '==')
# }


# permute([1, 2, 3])

# def permute(inputData, outputSoFar=[], stack = 1, iteration = 1):
#     # print('=======', inputData, outputSoFar, '======', 'stack begin', stack)
#     outputSizeToReach = len(inputData)
#     for elem in inputData:
#         # print('- iteration begin', iteration, '-', elem)
#         # print('- iteration begin', iteration, '-', elem, outputSoFar)
#         iteration += 1
#         if elem not in outputSoFar:
#             outputSoFar.append(elem)
#             # print('output', outputSoFar)
#             if len(outputSoFar) == outputSizeToReach:
#                 # print('end', outputSoFar)
#                 yield outputSoFar
#             else:
#                 # permute(inputData, outputSoFar, stack + 1)  # --- Recursion
#                 for permutation in permute(inputData, outputSoFar, stack + 1):
#                   yield permutation
#             outputSoFar.pop()
#         # iteration -=1
#         # print("- iteration end", iteration - 1, '-', inputData, outputSoFar)
#     # print('-- end loop --')
#     # print('== returnining to stack', stack - 1, '==')

# for i in permute([1,2,3]):
#   print(i)  # or whatever else you want to do with it
# # permute([1, 2, 3])

# def sockMerchant(n, ar):
#     pairs = 0
#     print(ar)
#     count_dict = {}
#     for num in ar:
#       print('num is', num, 'count is', count_dict)
#       if num not in count_dict:
#         count_dict[num] = True
#       else:
#         pairs += 1
#         count_dict.pop(num, None)
#     print(pairs)
#     return pairs
# sockMerchant(4, [10,20,20,10,10,30,50,10,20])
# newarr = [1,2,3]
# newlist = [num + 2 for num in newarr]
# print(newlist)

# Complete the jumpingOnClouds function below.
# def jumpingOnClouds(c):
#   i = 0
#   while i < len(c):
#     if i == 5:
#       i = 7
#     # other code
#     i += 1

# scp john.huynh@webcontent-webfront001.z10.zenimaxonline.com	:/usr/bin/minify /c/Users/verys_jhuyhn/projects/zenimax/scripts
