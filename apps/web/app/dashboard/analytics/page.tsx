import { Sidebar } from '../../../components/sidebar';

export default function AnalyticsPage() {
  return (
    <div className="min-h-screen bg-slate-950 text-slate-100">
      <div className="grid min-h-screen grid-cols-[280px_1fr]">
        <Sidebar />
        <main className="p-8">
          <section className="rounded-3xl border border-slate-800 bg-slate-900/90 p-8">
            <h1 className="text-3xl font-semibold">Analytics</h1>
            <p className="mt-3 text-slate-400">Track document ingestion, chat usage, and retrieval volume.</p>
            <div className="mt-8 grid gap-6 lg:grid-cols-2">
              <div className="rounded-3xl border border-slate-800 bg-slate-950 p-6">Sessions created: 0</div>
              <div className="rounded-3xl border border-slate-800 bg-slate-950 p-6">Documents indexed: 0</div>
            </div>
          </section>
        </main>
      </div>
    </div>
  );
}
