# Internal Link Graph
`NODE = URL / Page`; `EDGE = Internal Link`. Edge states: `EXISTING`, `PLANNED`, `REMOVED`, `BROKEN`, `REDIRECTED`, `UNKNOWN`. Maintain existing, planned and after-change views. Unknown metrics stay `UNKNOWN`. Graph operations are `FULL_BUILD`, `FULL_REFRESH`, `INCREMENTAL_UPDATE`, `REUSE`.
