select ph.ticker, ph.close_price,ph.date
from price_history ph
inner join (
	select ticker, max(date) as max_date from price_history group by ticker
) latest on ph.ticker = latest.ticker and ph.date = latest.max_date;

select ts.sector, avg(ph.close_price) as avg_price
from price_history ph
join ticker_sectors ts on ph.ticker=ts.ticker
where ph.date >= (select max(date) from price_history) - interval 20 day
group by ts.sector;

select date, ticker, close_price,
(close_price - lag(close_price) over (partition by ticker order by date))/ lag(close_price) over (partition by ticker order by date) as daily_return
from price_history
order by ticker, date
limit 20;