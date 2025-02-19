import type { Metadata } from "next";
import { ThemeProvider } from 'next-themes';
import { Theme } from '@radix-ui/themes';
import "./globals.css";
import '@radix-ui/themes/styles.css';

export const metadata: Metadata = {
  title: "CocoIndex",
  description: "Indexing infra for AI with exceptional velocity",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body>
        <ThemeProvider
          attribute="class"
          defaultTheme="system"
          enableSystem={true}
          storageKey="theme"
          disableTransitionOnChange
        >
          <Theme accentColor="violet">
            {children}
          </Theme>
        </ThemeProvider>
      </body>
    </html>
  );
}
