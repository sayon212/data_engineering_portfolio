SELECT 
    TopOne(event_id) OVER (ORDER BY trading_timestamp asc) as [id],
    System.Timestamp AS WindowEndTime,
    symbol,
    MAX(ltp) as high,
    MIN(ltp) as low,
    AVG(ltp) as avg,
    SUM(volume) as total_volume,
    SUM(num_trade) as total_trade,
    TopOne(ltp) OVER (PARTITION BY TumblingWindow(second,30) ORDER BY trading_timestamp asc) as open_price,
    TopOne(ltp) OVER (PARTITION BY TumblingWindow(second,30) ORDER BY trading_timestamp desc) as close_price
INTO ohcl
    FROM stockshub
    TIMESTAMP BY trading_timestamp
    GROUP BY symbol,TumblingWindow(second,30);