mkdir -p tbls


ls ./tbls/*.tbl \
  |  parallel -n 1 \
  'python ft.py {} ' \
  > tmp.tbl

head -n 1 tmp.tbl > all.tbl
cat tmp.tbl | grep -vw footprint_codes >> all.tbl 



exit 

cat ./bams.fofn |
  parallel -n 1 \
  "/mmfs1/gscratch/stergachislab/mvollger/projects/fibertools-rs/target/release/ft foot -b ./E.bed -y ./E.yaml {} > tbls/E-box.{/.}.tbl"


cat ./bams.fofn |
  parallel -n 1 -k \
  "/mmfs1/gscratch/stergachislab/mvollger/projects/fibertools-rs/target/release/ft foot -b ./C.bed -y ./C.yaml {} > tbls/CCAAT.{/.}.tbl" 


