# IBVAP - System Architecture (Step 3)

This is the master reference every team should check before writing code
that crosses a team boundary. It mirrors the Consolidated Data Flow at the
end of the Master Implementation Plan.

## The three tracks and the shared layer

```
                         shared/  (Phase 0 - frozen contracts)
                  schemas, fixtures, auth, config
                              |
        -------------------------------------------------
        |                    |                           |
   perception/           reasoning/                  platform/
   (Team 1)               (Team 2)                    (Team 3)
   Steps 5-17            Steps 18-32                 Steps 33-44
   "the eyes"             "the brain"              "the nervous system"
        |                    |                           |
        | Contract A->B      | Contract B->C              |
        |------------------->|--------------------------->|
        |  detection/track   |     alert events            |
        |  events            |                             |
        |                    |<----------------------------|
        |                    |  identity_read_schema /      |
        |                    |  read_api_contract (Team 3   |
        |                    |  reads Team 2's identity +   |
        |                    |  adjacency/metrics data      |
        |                    |  directly, not via alerts)   |
        |                    |                             |
        |<-------------------|                             |
        |  camera_health_schema (Team 1 publishes,          |
        |  Team 2 consumes for Steps 29/30; Team 3's         |
        |  edge write-ahead queue appends queue_depth        |
        |  when co-resident on an edge device - see edge/)   |
```

## Key rule

`shared/` is jointly owned. Once Phase 0 is done and all three teams
start building, nobody edits `shared/schemas/`, `shared/auth/`, or
`shared/config/` unilaterally - a change there is a cross-team
conversation, because all three tracks depend on those shapes staying
stable.

See the full Master Implementation Plan document for the complete
51-step breakdown and the Parallel Team Execution Plan for how the
three tracks build independently against these contracts.
