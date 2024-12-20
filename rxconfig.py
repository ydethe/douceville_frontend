import reflex as rx


class DvConfig(rx.Config):
    SUPABASE_URL: str
    SUPABASE_KEY: str


config = DvConfig(
    app_name="douceville_frontend",
    SUPABASE_URL="https://pmudhlqdazamugrmpkiu.supabase.co",
    SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBtdWRobHFkYXphbXVncm1wa2l1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTg3MDIxNzUsImV4cCI6MjAzNDI3ODE3NX0.ASOy8AW85AVPm6t7kKkyb14IVU_L_ZRUTPVjnlK8ZKg",
)
