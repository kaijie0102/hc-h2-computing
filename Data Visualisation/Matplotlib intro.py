import matplotlib.pyplot as plt 

x = [1,2,3]         #Data given
y = [10,11,12]
x2 = [1,2,3]
y2 = [4,5,6]

plt.plot(x,y,'yd-.',label='first graph')      #plot with symbols; bo for blue circle, r+ is red cross
plt.plot(x2,y2,'k*:',label='second graph')
#plt.bar(x,y,color='green')
"""
Type of graph: plot: line
               bar: bar graph
               hist: histogram
               

Colours : Red, Blue, Green, Cyan , Magenta, Yellow, Black (k), White

line style: -- : dotted line
            - : Normal straight line
            -. : dash-dot
            : : dot-dot
            
Marker: + : Crosses
        O : Dots
        ^ : Triangles
        . : point
        v : Inverted triangle
        s : Square
        8 : Octagon
        * : Star
        p : Pentagon
        d : Diamond
"""

plt.title('IM TILTED\nNOT')     #Title;Subtitle
plt.legend()        #Complements 'label' to label graph

plt.show()  #Always at the last line
