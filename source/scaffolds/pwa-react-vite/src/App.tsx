export function App() {
  return (
    <main className="app-shell">
      <header className="hero-card">
        <span className="pill">PWA bootstrap</span>
        <h1>__PROJECT_NAME__</h1>
        <p>__PROJECT_PURPOSE__</p>
      </header>
      <section className="status-grid">
        <article>
          <h2>Installability</h2>
          <p>manifest.webmanifest and service worker placeholders are included.</p>
        </article>
        <article>
          <h2>Runtime</h2>
          <p>__LANGUAGE__ / __FRAMEWORK__</p>
        </article>
        <article>
          <h2>Deploy</h2>
          <p>__DEPLOYMENT_TYPE__</p>
        </article>
      </section>
    </main>
  );
}
