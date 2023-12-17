-- SQLite
SELECT Method, Dataset, ConfusionMatrix, Loss, Acc, AUC, AP, FrameConfusionMatrix, FrameAUC, FrameACC, Description
FROM Results
where method = "efficientnetb1_lstm_dfdc"
order by AUC desc
