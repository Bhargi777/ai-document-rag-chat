import { Sidebar } from '@/components/sidebar';

export default function ChatPage() {
  return (
    <div className="min-h-screen bg-slate-950 text-slate-100">
      <div className="grid min-h-screen grid-cols-[280px_1fr]">
        <Sidebar />
        <main className="p-8">
          <section className="rounded-3xl border border-slate-800 bg-slate-900/90 p-8">
            <h1 className="text-3xl font-semibold">Chat</h1>
            <p className="mt-3 text-slate-400">Ask questions about your uploaded documents.</p>
            <div className="mt-8 rounded-3xl border border-slate-700 bg-slate-950 p-6">
              <p className="text-slate-400">Chat interface coming soon with streaming AI responses.</p>
            </div>
          </section>
        </main>
      </div>
    </div>
  );
}
