select type,COUNT(*) as data_count
from {{ ref('feature')}}
group by type