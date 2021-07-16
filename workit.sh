#!/usr/bin/bash

# WorkIt
#=== ---- ==== ---- ==== ---- ==== ---- ==== ---- ==== ---- ==== ---- ==== ---- 
#   created by: Arlo Gittings
#	created on: 2021-07-15
#   last modified: 2021-07-15
#   description:
#       Shellscript version of workit, it just calls vim if the file 
#       exists or makedailies if it doesn't.
#=== ---- ==== ---- ==== ---- ==== ---- ==== ---- ==== ---- ==== ---- ==== ----
base_dir="${DOCS}/dailies"
today=`date +%Y/%m/%d`
file="tasks.csv"
fq_file=${base_dir}/${today}/${file}

function makedailies(){
	mkdir -p ${base_dir}/${today}
	for template in `ls ${base_dir}/templates`;do
		cp ${base_dir}/templates/${file} ${fq_file}
	done
}

if [ ! -d ${base_dir}/${today} ]; then
  	makedailies  
else
    if [ ! -e ${fq_file} ];then
		cp ${base_dir}/templates/${file} ${fq_file}
	fi
fi

/usr/bin/nvim  $fq_file

