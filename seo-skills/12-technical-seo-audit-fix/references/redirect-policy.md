# Redirect Policy
Detect redirect chains and loops and prefer one-hop redirects where justified.
Actions: KEEP, CREATE_301, CREATE_302, UPDATE_EXISTING, REMOVE_REDIRECT, FLATTEN_CHAIN, BLOCK_FOR_OWNERSHIP, INVESTIGATE.
Creation/removal/change of live redirects is approval-gated. Low-confidence ownership-changing redirect recommendations are blocked.
