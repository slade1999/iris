from collections import Counter
import math
import csv

def dot( v, w ):
    return sum( v_i * w_i for v_i, w_i in zip( v, w ))

def sum_of_squares( v ):
    return dot( v, v )

def vector_subtract( v, w ):
    return [ v_i - w_i for v_i, w_i in zip( v, w )]

def squared_distance( v, w ):
    return sum_of_squares( vector_subtract( v, w ))

def distance( v, w ):
    return math.sqrt( squared_distance( v, w ))

def majority_vote( labels ):
    vote_counts = Counter(labels)
    winner, winner_count = vote_counts.most_common(1)[0]
    num_winners = len( [count for count in vote_counts.values()
                                        if count == winner_count ])
    if num_winners == 1:
        return winner
    else:
        return majority_vote(labels[:-1])

def knn_classify( k, labeled_points, new_point ):
    by_distance = sorted( labeled_points, 
                         key=lambda lp: distance(lp[0], new_point))
    k_nearest_labels = [ lp[1] for lp in by_distance[:k]]
    return majority_vote(k_nearest_labels)

def ktest( vertebral_matrix ):
    for k in [ 1, 3, 5, 7 ]:
        num_correct = 0
        for vertebral_row in vertebral_matrix:
            pelvic_data, actual_diagnosis = vertebral_row
            other_vertebral_data = [ other_data for other_data in vertebral_matrix if other_data != vertebral_row ]
            predicted_diagnosis = knn_classify( k, other_vertebral_data, pelvic_data)
            if ( predicted_diagnosis == actual_diagnosis ):
                num_correct += 1
        
        print( k, "neighbor[s]:", num_correct, "correct out of", len( vertebral_matrix ) )

def Main():
    with open('iris.csv', 'r' ) as f:
        contents = csv.reader( f )
        vertebral_matrix = list()
        for row in contents:
            """just convert the first two string values in the row to float's"""
            """and put the two float's into a point""" 
            row = [ [float( row[0]), float( row[1])], row[2] ]
            vertebral_matrix.append( row )
    ktest( vertebral_matrix )

Main()