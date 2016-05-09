# Plunder

Library for making sense of [Agent Ransack](https://www.mythicsoft.com/agentransack) results. Very much a WIP.

If you're looking for a solid SQLite tool, check out [DB Browser for SQLite](http://sqlitebrowser.org/).

## Usage

```python
import plunder

plunder.add_results_to_db("Report.txt", override=True)
```

This reads the tab-delimited results into `plunder.sqlite` so you can query to your heart's content.

## License

See LICENSE for details.
