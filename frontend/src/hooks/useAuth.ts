import { useState } from "react";
import { api } from "../services/api";

interface AuthState {
  token: string | null;
  user: { email: string; full_name?: string } | null;
}

export function useAuth() {
  const [auth, setAuth] = useState<AuthState>({ token: null, user: null });

  const login = async (email: string, password: string) => {
    const form = new URLSearchParams({ username: email, password });
    const res = await fetch(`${import.meta.env.VITE_API_URL}/api/v1/auth/login`, {
      method: "POST",
      body: form,
    });
    const data = await res.json();
    const user = await api.get<AuthState["user"]>("/users/me", data.access_token);
    setAuth({ token: data.access_token, user });
  };

  const logout = () => setAuth({ token: null, user: null });

  return { ...auth, login, logout };
}
