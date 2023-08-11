-- SQLite
SELECT Method, AVG(AUC) as AvgAUC, AVG(Acc) as AvgACC
    FROM Results
    GROUP BY Method
    order by AvgAUC desc