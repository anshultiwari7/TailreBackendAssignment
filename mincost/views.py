# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import collections

from django.forms import forms
from django.shortcuts import render
from rest_framework.response import Response
import sys
import math
from rest_framework.views import APIView
#
# {
# "A":3,
# "B":0,
# "C":0,
# "D":12,
# "E":0,
# "F":0,
# "G":0,
# "H":0,
# "I":0
# }

totalwt = 0
def xyz(x_dict):

    values = []
    adj = [[0, 4, 0, 3],
           [4, 0, 3, 2.5],
           [0, 3, 0, 2],
           [3, 2.5, 2, 0]]
    def calcCost(w):
        global cost
        cost = 0
        if w <= 5:
            return 10
        w = w - 5
        cost = 10
        cost = cost + math.ceil(w / 5) * 8
        return cost


    def getTotalWeight(items):
        w = 0
        if 'A' in items:
            w = w + values[0]
        if 'B' in items:
            w = w + values[1]
        if 'C' in items:
            w = w + values[2]
        if 'D' in items:
            w = w + values[3]
        if 'E' in items:
            w = w + values[4]
        if 'F' in items:
            w = w + values[5]
        if 'G' in items:
            w = w + values[6]
        if 'H' in items:
            w = w + values[7]
        if 'I' in items:
            w = w + values[8]
        return w


    def min_cost(l1, s, items, w, l2):
        global cost
        cost = 0
        if len(l1) != 0:
            prev = l1[-1]
            cost = calcCost(w) * adj[prev][s]

        l1.append(s)
        # print l1

        if s == 0:
            if 'A' in items:
                w = w + values[0]
            if 'B' in items:
                w = w + values[1]
            if 'C' in items:
                w = w + values[2]
        elif s == 1:
            if 'D' in items:
                w = w + values[3]
            if 'E' in items:
                w = w + values[4]
            if 'F' in items:
                w = w + values[5]
        elif s == 2:
            if 'G' in items:
                w = w + values[6]
            if 'H' in items:
                w = w + values[7]
            if 'I' in items:
                w = w + values[8]
        elif s == 3:
            global totalwt
            if w == totalwt:
                # print(cost)
                l1.remove(s)
                return cost
            totalwt = totalwt - w
            w = 0

        big = sys.maxint
        for i in range(0, 4):
            # print "i="+str(i)
            if i not in l2:
                continue
            if i in l1 and i != 3:
                continue
            if adj[s][i] == 0:
                continue;
            # print "test="+str(i)
            cost1 = cost + min_cost(l1, i, items, w, l2)
            # print "cost=" + str(cost1)
            if cost1 < big:
                big = cost1

        l1.remove(s)
        return big


    # print "Enter elements in to be sent to the customer : "

    items = []

    for key in x_dict:
        if x_dict[key] == 0:
            del x_dict[key]
            values.append(0)
        else:
            items.append(key)
            values.append(x_dict[key])


    l2 = [3]

    cost = sys.maxint

    if 'A' in items or 'B' in items or 'C' in items:
        l2.append(0)

    if 'D' in items or 'E' in items or 'F' in items:
        l2.append(1)

    if 'G' in items or 'H' in items or 'I' in items:
        l2.append(2)

    # print l2

    for i in l2:
        global totalwt
        totalwt = getTotalWeight(items)
        # print i
        if i == 3:
            continue
        c1 = min_cost([], i, items, 0, l2)
        # print c1
        if c1 < cost:
            cost = c1

    return  cost



class cost(APIView):

    def get(self, request):
        unordered_dict ={"Hello JSON file just like given below, all items in order and their corresponding quantity/weight as per the customer requirement":" ",
"A":3,
"B":0,
"C":0,
"D":12,
"E":0,
"F":0,
"G":0,
"H":0,
"I":0
}       
        ordered_response = collections.OrderedDict(unordered_dict)
        return Response(ordered_response)
    def post(self, request):
        data = request.data
        print(data)
        output = {}
        d = collections.OrderedDict()
        d['A'] = data['A']
        d['B'] = data['B']
        d['C'] = data['C']
        d['D'] = data['D']
        d['E'] = data['E']
        d['F'] = data['F']
        d['G'] = data['G']
        d['H'] = data['H']
        d['I'] = data['I']
        for key in d:
            print (key)
        result = xyz(d)
        output['Minimum Cost'] = result
        return Response(output)



