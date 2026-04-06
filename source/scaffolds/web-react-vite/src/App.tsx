export function App() {
  return (
    <main className="app-shell">
      <section className="hero">
        <p className="eyebrow">__PROJECT_FAMILY__</p>
        <h1>__PROJECT_NAME__</h1>
        <p className="lead">__PROJECT_PURPOSE__</p>
      </section>
      <section className="info-grid">
        <article>
          <h2>Runtime</h2>
          <p>__LANGUAGE__ / __FRAMEWORK__</p>
        </article>
        <article>
          <h2>Deploy</h2>
          <p>__DEPLOYMENT_TYPE__</p>
        </article>
        <article>
          <h2>Integrations</h2>
          <p>__EXTERNAL_INTEGRATIONS__</p>
        </article>
      </section>
    </main>
  );
}
