import { Sidebar } from '@/components/sidebar';
import { ChatPanel } from '@/components/chat-panel';
import { fetchHealth } from '@/lib/api';

export default async function DashboardPage() {
  const health = await fetchHealth();
  const messages = [
    { role: 'assistant', text: 'Welcome! Upload documents to begin semantic search.' },
    { role: 'user', text: 'How does the RAG pipeline work?' },
  ];

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100">
      <div className="grid min-h-screen grid-cols-[280px_1fr]">
        <Sidebar />
        <main className="p-8">
          <div className="flex flex-col gap-6">
            <section className="rounded-3xl border border-slate-800 bg-slate-900/90 p-8">
              <h1 className="text-3xl font-semibold">Dashboard</h1>
              <p className="mt-2 text-slate-400">Backend status: {health.status}</p>
            </section>
            <section className="grid gap-6 lg:grid-cols-[1fr_1fr]">
              <div className="rounded-3xl border border-slate-800 bg-slate-900/90 p-8">
                <h2 className="text-xl font-semibold">Upload documents</h2>
                <p className="mt-3 text-slate-400">Upload your PDFs to create a searchable knowledge base.</p>
                <div className="mt-6 rounded-3xl border-2 border-dashed border-slate-700 p-8 text-center">
                  <p className="text-slate-500">Drag and drop PDF files here</p>
                </div>
              </div>
              <div className="rounded-3xl border border-slate-800 bg-slate-900/90 p-8">
                <h2 className="text-xl font-semibold">Recent activity</h2>
                <p className="mt-3 text-slate-400">Monitor ingestion and retrieval events for your workspace.</p>
                <div className="mt-6 grid gap-4">
                  <div className="rounded-2xl bg-slate-950 p-4">Document uploaded: quarterly-report.pdf</div>
                  <div className="rounded-2xl bg-slate-950 p-4">Chat session created: product-research</div>
                </div>
              </div>
            </section>
            <section>
              <h2 className="text-2xl font-semibold">Chat preview</h2>
              <ChatPanel messages={messages} />
            </section>
          </div>
        </main>
      </div>
    </div>
  );
}
