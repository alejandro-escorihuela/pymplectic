# 10-12-2020
# alex
# harP.plt
reset
#set term wxt persist
set term png
set output "kepNP08.png"
set palette defined (0 '#000090', 1 '#000FFF', 2 '#0090FF', 3 '#0FFFEE', 4 '#90FF70', 5 '#FFEE00', 6 '#FF7000', 7 '#EE0000', 8 '#7F0000')
# set grid
set style line 1  lt rgb '#0060AD'
set style line 2  lt rgb '#60AD00'
set style line 3  lt rgb '#AD0B00'
set style line 4  lt rgb '#E7E730'
set style line 5  lt rgb '#E730E7'
set style line 6  lt rgb '#30E7E7'
set style line 7  lt rgb '#707070'
set style line 8  lt rgb '#FF8E1E'
set style line 9  lt rgb '#202020'
set style line 10 lt rgb '#F000F0'

plot "../dat/r1_s2/kepl_cons_1000000_001.dat" u (log10($1)):(log10(abs($3))) w l t "r1 s2", \
     "../dat/sc_3_4/kepl_cons_1000000_001.dat" u (log10($1)):(log10(abs($3))) w l t "sc 34", \
     "../dat/ssc_3_4/kepl_cons_1000000_001.dat" u (log10($1)):(log10(abs($3))) w l t "ssc 34"
