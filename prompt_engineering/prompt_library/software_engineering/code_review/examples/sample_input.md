# Code Review Example — Sample Input

This is a deliberately small, illustrative Express-style endpoint for review practice. It is not intended for production use.

## Context supplied to the reviewer

- **Language/framework:** JavaScript with Express-style routing.
- **Intended behavior:** Update the display name for the user identified by the route parameter.
- **Database API:** `db.query(sql)` executes the supplied SQL string. No parameter-binding API is shown in this example.
- **Authentication/authorization context:** Not supplied. The snippet may be mounted behind router-level middleware; that cannot be determined here.
- **Review focus:** Security and error handling.

## Source code

```js
router.post('/users/:userId/profile', async (req, res) => {
  const userId = req.params.userId;
  const { displayName } = req.body;

  const sql = `
    UPDATE users
    SET display_name = '${displayName}'
    WHERE id = ${userId}
  `;

  try {
    await db.query(sql);
    return res.status(200).json({ message: 'Profile updated' });
  } catch (error) {
    return res.status(500).json({ error: error.message });
  }
});
```

## Review boundary

Review only the code and context above. Do not assume that authentication, authorization, input validation, or additional database protections exist or do not exist outside the snippet. The database call is described as executing the interpolated SQL string, with no parameter binding shown.
