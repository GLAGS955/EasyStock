const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000/api/v1";

export const api = {
  async post<T>(path: string, body: unknown, token?: string): Promise<T> {
    const res = await fetch(`${API_URL}${path}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        ...(token ? { Authorization: `Bearer ${token}` } : {}),
      },
      body: JSON.stringify(body),
    });
    if (!res.ok) throw new Error(await res.text());
    return res.json();
  },

  async get<T>(path: string, token?: string): Promise<T> {
    const res = await fetch(`${API_URL}${path}`, {
      headers: token ? { Authorization: `Bearer ${token}` } : {},
    });
    if (!res.ok) throw new Error(await res.text());
    return res.json();
  },
};
