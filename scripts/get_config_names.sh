for file in ~/.config/*
do
	# do something on "$file"
	cat "$file" >> $1
	# echo "$file"
done
