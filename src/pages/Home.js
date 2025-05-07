import React, { useState } from "react";

export default function Home() {
  const [count, setCount] = useState(0);
  return (
    <div>
      <h1>Home Page</h1>
      <p>Contador: {count}</p>
      <button onClick={() => setCount(count + 1)}>Incrementar</button>
    </div>
  );
}
