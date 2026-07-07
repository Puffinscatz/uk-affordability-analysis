-- Latest affordability ranking by region

SELECT
    area_name,
    time_period,
    rental_price,
    median_monthly_pay,
    rent_to_pay_percent
FROM affordability_data
WHERE time_period = (
    SELECT MAX(time_period)
    FROM affordability_data
)
ORDER BY rent_to_pay_percent DESC;

-- Average affordability pressure by region over the full period

SELECT
    area_name,
    ROUND(AVG(rent_to_pay_percent), 2) AS average_rent_to_pay_percent
FROM affordability_data
GROUP BY area_name
ORDER BY average_rent_to_pay_percent DESC;

-- Rent growth and wage growth by region
SELECT
    area_name,
    first_rent,
    latest_rent,
    rent_growth_percent,
    first_pay,
    latest_pay,
    pay_growth_percent,
    affordability_change_pp
FROM affordability_growth_summary
ORDER BY affordability_change_pp DESC;