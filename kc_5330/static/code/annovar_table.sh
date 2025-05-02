perl annovar/table_annovar.pl cdkn2a_2b.vcf \
annovar/humandb/ \
-buildver hg19 \
-out cdkn2a_2b \
-protocol refGeneWithVer \
-operation g \
-remove -polish -vcfinput -nastring .