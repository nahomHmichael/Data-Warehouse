select type , AVG(traveled_d) as dist_avg
from {{ ref('feature') }}
Group by type