import React from 'react'
import { render, screen } from '@testing-library/react'
import { Sidebar } from '../components/sidebar'

describe('Sidebar', () => {
  it('renders all dashboard links and theme toggle', () => {
    render(<Sidebar />)

    expect(screen.getByText('Dashboard')).toBeInTheDocument()
    expect(screen.getByText('Upload')).toBeInTheDocument()
    expect(screen.getByText('Chat')).toBeInTheDocument()
    expect(screen.getByText('Documents')).toBeInTheDocument()
    expect(screen.getByText('Analytics')).toBeInTheDocument()
    expect(screen.getByRole('button')).toHaveTextContent('Dark mode')
  })
})
