# Expected Findings — Code Review Example

This is a manually reasoned reference for the [sample input](sample_input.md). It defines findings that are supported by the stated example context. It is not a model output, an evaluation result, or proof that the prompt detects these issues.

## Finding 1 — SQL injection through interpolated values

- **Expected severity:** HIGH
- **Expected status:** CONFIRMED
- **Evidence:** `displayName` is inserted directly into a quoted SQL string, and `userId` is inserted directly into the `WHERE id = ...` expression. The supplied context states that `db.query(sql)` executes this SQL string and shows no parameter binding.
- **Reasoning:** Untrusted request values are incorporated into SQL syntax. Crafted input may alter the statement rather than remain data.
- **Impact:** An attacker may manipulate the update query, potentially changing unintended records or otherwise affecting database integrity. Exact exploitability and database permissions are outside the supplied context.
- **Targeted recommendation:** Use the database driver's parameterized-query interface for both values; validate `userId` against the expected identifier format and validate `displayName` according to application rules. Do not build SQL by string interpolation.
- **Verification:** Add tests with quotes and SQL metacharacters in both request fields and assert they are passed as parameter values, not interpreted as SQL syntax.

## Finding 2 — Database error details returned to the client

- **Expected severity:** MEDIUM
- **Expected status:** CONFIRMED
- **Evidence:** `return res.status(500).json({ error: error.message });`
- **Reasoning:** The raw error message from the database layer is returned in the HTTP response.
- **Impact:** Depending on the database driver and error, the response may disclose schema, query, host, or implementation details that help an attacker understand the system. The exact contents of a particular error are not shown.
- **Targeted recommendation:** Return a generic client-facing error and log diagnostic details securely on the server, avoiding secrets and sensitive data in logs.
- **Verification:** Simulate a database failure and assert that the client receives a generic response while server-side diagnostics remain access-controlled.

## Context-dependent concern — Authorization for the target user

- **Expected severity:** POTENTIAL / requires verification; do not assign a confirmed severity from this snippet alone.
- **Expected status:** POTENTIAL
- **Evidence:** The handler updates the row selected by `req.params.userId`; no ownership check is visible in the supplied handler.
- **Missing context:** The sample explicitly says router-level authentication or authorization middleware may exist but is not supplied.
- **Reasoning:** If no authorization check ensures the caller may update the requested user, changing the route parameter could allow one user to modify another user's profile. The snippet alone cannot establish whether such a check exists elsewhere.
- **Verification:** Inspect route mounting, authentication middleware, and authorization policy; test that a user cannot update another user's record.

## Expected review behavior

A careful review should identify the two confirmed issues, distinguish the authorization concern as potential, cite the supplied statements, prioritize the findings, and recommend focused fixes. It should not claim that authentication is absent or that the endpoint is definitely exploitable through broken access control without the missing context.
