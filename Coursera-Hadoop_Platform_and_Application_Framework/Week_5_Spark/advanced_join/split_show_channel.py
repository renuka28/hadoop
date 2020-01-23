def split_show_channel(line):
	show, channel=line.split(',')
	if(channel == 'BAT'):
		return (show, channel)
