echo "Downloading benchmark files for TPC-H benchmark ..."
pip install gdown==4.7.1

# echo "Downloading benchmark data ..."
# gdown "https://drive.google.com/uc?id=1BjHTNXwGoZIkadECex3PzMdYuSJ1NCOp" -O /tmp/tpchdata.tar.gz

cd /tmp

echo "Decompressing data ..."
tar xvf tpchdata.tar.gz

cd tpchdata

echo "Installing TPC-H on PostgreSQL ..."
createdb tpch

echo "Creating database schema ..."
psql -d tpch -f schema.sql

echo "Loading data ..."
psql -d tpch -f loadpg.sql

echo "Indexing data ..."
psql -d tpch -f index.sql

echo "✅ TPC-H setup complete!"
