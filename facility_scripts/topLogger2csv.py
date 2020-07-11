#!/usr/bin/env python

import sys

if __name__ == '__main__':
	if len(sys.argv) <= 2:
		print "not enought files given as paramater."
		sys.exit(0)
	fr = open(sys.argv[1],"r")
	fw = open(sys.argv[2],"w")
	fr_data = fr.read()
	fr.close()
	fr_data_split = fr_data.split("top ")

	delim = "\t"
	delim2 = ", "
	fw.write("load_avg" + delim2 + "running" + delim2 + "threads"
		+ delim2 + "sleeping" + delim2 + "threads" + delim2 + "stopped"
		+ delim2 + "threads" + delim2 + "zombies" + delim2 + "cpu_be"
		+ delim2 + "cpu_sy" + delim2 + "cpu_ni" + delim2 + "cpu_un" + delim2 + "cpu_wa"
		+ delim2 + "cpu_hi" + delim2 + "cpu_si" + delim2 + "cpu_st"
		+ delim2 + "mem_used" + delim2 + "mem_free" + delim2 + "mem_buffered"
		+ delim2 + "swap_used" + delim2 + "swap_free" + delim2 + "mem_cached" + "\n")
	for i in range(2,len(fr_data_split)):
	
		cur = fr_data_split[i]
		print str(i) + " " + cur
		cur = cur.replace("\n", ", ")
		cur_split = cur.split(", ")
		# print cur_split

		load_avg = (cur_split[3].split(":"))[1]
		running = (cur_split[7].split("r"))[0]
		sleeping = (cur_split[8].split("s"))[0]
		stopped = (cur_split[9].split("s"))[0]
		zombie = (cur_split[10].split("z"))[0]

		cpu_be = (((cur_split[11].split(":"))[1]).split("b"))[0]
		cpu_sy = (cur_split[12].split("s"))[0]
		cpu_ni = (cur_split[13].split("n"))[0]
		cpu_un = (cur_split[14].split("u"))[0]
		cpu_wa = (cur_split[15].split("w"))[0]
		cpu_hi = (cur_split[16].split("h"))[0]
		cpu_si = (cur_split[17].split("s"))[0]
		cpu_st = (cur_split[18].split("s"))[0]

		mem_used = (cur_split[20].split("u"))[0]
		mem_free = (cur_split[21].split("f"))[0]
		mem_buffers = (cur_split[22].split("b"))[0]

		swap_used = (cur_split[24].split("u"))[0]
		swap_free = (cur_split[25].split("f"))[0]
		
		mem_cached = (((cur_split[25].split("."))[1]).split("c"))[0]

		text = (str(load_avg) + delim + str(running) + delim + str(sleeping) + delim + str(stopped) + delim + str(zombie) + delim 
			+ str(cpu_be) + delim + str(cpu_sy) + delim + str(cpu_ni) + delim + str(cpu_un) + delim + str(cpu_wa) + delim + str(cpu_hi) + delim
			+ str(cpu_si) + delim + str(cpu_st) + delim + str(mem_used) + delim + str(mem_free) + delim + str(mem_buffers) + delim
			+ str(swap_used) + delim + str(swap_free) + delim + str(mem_cached) + str("\n"))
		text = text.replace(",",".")
		text = text.replace("\t", ", ")
		print text
		fw.write(text)

	fw.close()
	sys.exit(0)