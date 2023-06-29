USE [BWorks]
GO

/****** Object:  Table [dbo].[Transactions]    Script Date: 23-06-2023 22:52:47 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Transactions](
	[TransactionId] [int] IDENTITY(1,1) NOT NULL,
	[UserId] [int] NULL,
	[BicycleId] [int] NULL,
	[BicycleNo] [int] NULL,
	[IsBuy] [bit] NOT NULL,
	[IsDonate] [bit] NOT NULL,
	[Address] [varchar](max) NOT NULL,
	[ContactId] [int] NOT NULL,
	[DateOfDonate] [datetime] NULL,
	[DateOfBuy] [datetime] NULL,
	[Status] [bit] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[TransactionId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO

ALTER TABLE [dbo].[Transactions]  WITH CHECK ADD FOREIGN KEY([BicycleId])
REFERENCES [dbo].[Bicycles] ([BicycleId])
GO

ALTER TABLE [dbo].[Transactions]  WITH CHECK ADD FOREIGN KEY([UserId])
REFERENCES [dbo].[Users] ([UserId])
GO

