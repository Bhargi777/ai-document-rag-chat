interface ChatPanelProps {
  messages: Array<{ role: 'user' | 'assistant'; text: string }>;
}

export function ChatPanel({ messages }: ChatPanelProps) {
  return (
    <div className="space-y-4 rounded-3xl border border-slate-800 bg-slate-900/95 p-6">
      {messages.map((message, index) => (
        <div key={index} className="space-y-2">
          <p className="text-xs uppercase tracking-[0.2em] text-slate-500">{message.role}</p>
          <div className="rounded-2xl bg-slate-950 p-4 text-slate-100">{message.text}</div>
        </div>
      ))}
    </div>
  );
}
