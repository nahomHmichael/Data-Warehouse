select type,
        AVG(avg_speed) as speed_avg
    from {{ ref('feature')}}
    group by type

